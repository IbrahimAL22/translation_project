from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import json

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\Ibrahim\Desktop\rag\local_model\tokenizer")
model = AutoModelForSeq2SeqLM.from_pretrained(r"C:\Users\Ibrahim\Desktop\rag\local_model\model")

@csrf_exempt
def translate_text(request):
    if request.method == 'POST':
        tounsi_text = request.POST.get('tounsi_text', '')
        
        if not tounsi_text:
            return render(request, 'translator/translate_form.html', {'error': 'No text provided'})
        
        # Encode the input text and generate the translation
        inputs = tokenizer.encode(tounsi_text, return_tensors="pt", max_length=512, truncation=True)
        outputs = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return render(request, 'translator/translate_form.html', {'translated_text': translated_text})
    
    return render(request, 'translator/translate_form.html')
