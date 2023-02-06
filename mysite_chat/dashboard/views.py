from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm
import openai

def index(request):
    if request.method == 'POST':
    	# Get the user-entered topic
        topic = request.POST.get('topic')
        funny = request.POST.get('funny')
        hashtag = request.POST.get('hashtag')


        form = TopicForm(request.POST)

       

        openai.api_key = "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"
        model_engine = "text-davinci-002"

        prompt = f"write three tweets about {topic}. {hashtag} hashtags at the end. Keep it clear and concise. Include superlatives. Use strong verbs and limit adjectives and adverbs. Keep the tone conversational. Make sure the tweet is no more than 150 characters. Make one of the three tweets include imperative phrases. Make it sound personal. Include specific names and statistics if it is relevant. Make it {funny}. Separate each tweet with Tweet #1:, Tweet #2:, and Tweet #3."

        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        tweet = completions.choices[0].text

        return render(request, 'dashboard/index.html', {'tweet': tweet})
    else:
        form = TopicForm()

    return render(request, 'dashboard/index.html')
