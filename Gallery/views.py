from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Painting,Category
from .forms import PaintingForm
from utils.style_transfer import * 
from ImageArt.settings import MEDIA_ROOT,MEDIA_URL,AWS_STORAGE_BUCKET_NAME,AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
import boto3
from PIL import Image
import io 
import urllib.request
import os
import glob
import random
import string
import requests


# Create your views here.


"dimesnions for painting"
new_width  = 380
new_height = 512

# hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')





## utils for getting s3 uploaded pics urls :
s3 = boto3.client('s3')

client = boto3.client('s3',
                          region_name='eu-west-2',
                          
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)



def get_s3_img_url():

    return(NotImplemented)




def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)
    


                 

def all_paintings(request):
    """ A view to show all paintings, including sorting and search queries """

    paintings = Painting.objects.filter(Add_to_Gallery=True)
    query = None
    categories=None
    sort = None
    direction = None

    if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    paintings = paintings.annotate(lower_name=Lower('name'))
                if sortkey == 'category':
                    sortkey = 'category__name'
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                paintings = paintings.order_by(sortkey)

            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                print(categories)
                paintings = paintings.filter(category__name__in=categories)
                print(paintings)
                categories = Category.objects.filter(name__in=categories)


            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('paintings'))
                
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                paintings = paintings.filter(queries)

    current_sorting = f'{sort}_{direction}'  

    context = {
        'paintings': paintings,
        'search_term': query,
         'current_categories': categories,
         'current_sorting': current_sorting,
         
    }

    return render(request, 'Gallery/gallery.html', context)

    


def product_detail(request, painting_id):
    """ A view to show individual product/painting details """
    print(painting_id)

    product = get_object_or_404(Painting, pk=painting_id)

    context = {
        'product': product,
    }

    return render(request, 'Gallery/product_detail.html', context)



@login_required
def add_painting(request):
    """ Add a product to the store """
    form = PaintingForm()

    "get a random string for file names"
    file_name_append=get_random_string(3)
    
    template = 'Gallery/add_painting.html'
    template2 = 'Gallery/painting_no_gallery.html'
    template3 ='Gallery/painting_price_form.html'

    

    "if add to gallery is not checked , simply process the images and output to html , else  save each image  and generate a different template" 
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        print("In request post")
        if form.is_valid():
            
            "check if add to gallery is not added  and simply render no saving images"
            add_to_gallery=form.cleaned_data['Add_to_Gallery']
            print(add_to_gallery)
           
            

            ## Get file names  and url paths from s3
            content_filename=request.FILES['upload_pic'].name
            style_filename=request.FILES['style_pic'].name
            content_path=MEDIA_URL+'Gallery_images/Upload_pic/'+request.FILES['upload_pic'].name
            style_path=MEDIA_URL+'Gallery_images/Style_pic/'+request.FILES['style_pic'].name
            print("my content path"+str(content_path))
            print("my style path :",str(style_path))

            ### Save url files for upload and style images , process using tensorflow and delete


            r = requests.post(
            "https://api.deepai.org/api/fast-style-transfer",
            data={
                'content': content_path,
                'style': style_path,
            },
            headers={'api-key': os.getenv('deepai_apikey')}

            )

            
            
            displayurl=r.json()['output_url']
            
           
         
           # Load upload image from s3
            

            # upload_image=load_img(content_path)
            # style_image=load_img(style_path)
            # stylized_image = hub_model(tf.constant(upload_image), tf.constant(style_image))[0]
            # l=tensor_to_image(stylized_image)

            # #Save the Painting in the media folder , to upload to s3 and then delet 
            
          
            # "resize Image"
            # l= l.resize((new_width, new_height), PIL.Image.ANTIALIAS)
            

            # ### Read data to temporary buffer and save to s3
            # buffer = io.BytesIO()
            # l.save(buffer,format="jpeg")
            # buffer.seek(0) # rewind pointer back to start
            # s3.put_object(
            #     Bucket=AWS_STORAGE_BUCKET_NAME,
            #     Key='media/Gallery_images/Paintings/{}'.format(content_filename+"_"+str(file_name_append)),
            #     Body=buffer,
            #     ContentType='image/jpeg',
            # )


         
            
            
            #After painitings saved remove :: media files 





            
           
            
            if not add_to_gallery :
                

                # Resize image     
                 
                 context = {
        
                        'stylised_painting': displayurl,
                    }

                 return render(request, template2,context)
            else: 
                print("IN add Gallery")
                
                
                
                
                "Combine style and upload image save to media and upload"
                content_image_pil = PIL.Image.open(request.FILES['upload_pic'])
                style_image_pil = PIL.Image.open(request.FILES['style_pic'])

                print("l1")
                "Combine the image and save image url "
                combined_image=get_concat_v_resize(content_image_pil, style_image_pil, resize_big_image=False)
                combined_image=combined_image.resize((new_width, new_height), PIL.Image.ANTIALIAS)
                upload_name=request.FILES['upload_pic'].name
                upload_name=upload_name.split(".")[0]
                style_name=request.FILES['style_pic'].name

                combined_image_save=MEDIA_ROOT+'/''Gallery_images/Upload_style_combined/'+upload_name+"_"+style_name
                display_combinedurl=MEDIA_URL+'Gallery_images/Upload_style_combined/'+upload_name+"_"+style_name   
                path_combinedimage_AWS='media/Gallery_images/Upload_style_combined/'+upload_name+"_"+style_name  
                "Save in form for combined image"
                print("l2") 

                 ### Read data to temporary buffer and save to s3
                buffer = io.BytesIO()
                combined_image.save(buffer,format="jpeg")
                buffer.seek(0) # rewind pointer back to start
                s3.put_object(
                    Bucket=AWS_STORAGE_BUCKET_NAME,
                    Key='media/Gallery_images/Upload_style_combined/{}'.format(upload_name+"_"+style_name),
                    Body=buffer,
                    ContentType='image/jpeg',
                )
                print("saved joined images")
                "process the  files  and render "
                saved_form=form.save()

                saved_form.image=displayurl
                saved_form.upload_style_combined=display_combinedurl
                saved_form.save()

                "Take the user to add name description and rating"
                context={
                   
                    'form_with_painting': saved_form,
                    'stylised_painting' : displayurl

                }


                return redirect('paintings')    


    

    "pass painting into context"
    context = {
        
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_painting(request, painting_id):



    """ Edit a product in the store """
    product = get_object_or_404(Painting, pk=painting_id)
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = PaintingForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'Gallery/edit_painting.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_painting(request, painting_id):
    """ Delete a product from the store """
    product = get_object_or_404(Painting, pk=painting_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('paintings'))