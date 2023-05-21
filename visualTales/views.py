from django.shortcuts import render
import openai, os, requests
from dotenv import load_dotenv
from django.core.files.base import ContentFile
from .models import Image
from django.http import HttpResponse
from .styles import Prompt_Stylizer
from .textParser import countPuncts # Counts sentences
# Create your views here.

def members(request):
    return HttpResponse("Hello world!")
load_dotenv()

api_key= os.getenv("OPENAI_KEY",None)
openai.api_key=api_key

def generate_image_from_txt(request):
  writer = Prompt_Stylizer()
  userStyle = 'realistic' # Input the user's requested style here
  obj = None
  img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3ItjUjmdyS3oifHWUhSGsSpNphIZ38hZ3Obdz2FjU&s'
  if api_key is not None and request.method == 'POST':
    user_input = request.POST.get('user_input')
    parsedPrompt = writer.generateOutputPrompt(userStyle, user_input)
    response = openai.Image.create(
      prompt=parsedPrompt,#user_input,
      n=1,
      size='512x512'
    )
    print(response)
    print(parsedPrompt)
    
      
    img_url = response["data"][0]["url"]
    print(img_url)
    response = requests.get(img_url)
    img_file = ContentFile(response.content)
    
    count = Image.objects.count() 
    fname = f"image-{count}.jpg"

    obj=Image(phrase=user_input)
    obj.ai_image.save(fname, img_file)
    obj.save()
    print(obj)
  return render(request, "main.html", {"object": obj, "img_url": img_url})

