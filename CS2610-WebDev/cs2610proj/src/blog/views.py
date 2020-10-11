from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from .models import Blog, Comment
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render
from time import strftime

filler = [
    "Hello World! Once again It's time for deep thoughts. Today let's think about who and what we are, as well as who"
    " and what we want to be. I am always thinking about this. Who am I? What is the sum of my actions? Who is it that"
    " others see in me that I don't necessarily see in my self? Though the most important question I seem to ask myself"
    " a lot is, \"Am I the hero, the villain, or the bystander of my story?\"I mean think about it carefully. Do I make"
    " the right choices for the right reasons? I like to think so but on closer reflection I feel like sometimes I am"
    " just going through the motions and doing what is expected of me merely because it's expected. I believe that it"
    " takes action to prove our worth one way or the other, because without it we are truly just bystanders and on"
    " lookers in our own story. We should all strive to truly play the main of our stories otherwise, what was the"
    " point of having them in the first place? And, what are they even our stories at that point?Though, once you pick"
    " a path, how do you know it's the right one? Well, in the end that comes down to what you believe to be right now"
    " doesn't it?",
    "Today was interesting to say the least. I went to a new movie called The Upside. It was extremely funny and deep"
    " in a way. To those who are reading this they should totally see it. I also pondered and learned a lot about what"
    " it takes to do the right thing and take pride in that no matter the consequences.It's not always easy to live"
    " your life to the fullest, strive to do what's right, and take care of those who need you but make it difficult"
    " no matter what you do.I have been working extremely hard to succeed in this balancing act with out much success,"
    " but every time that the light shines through it brings a sense of satisfaction and happiness of such epic"
    " proportions that it makes all of the struggling worth it. After realizing what needed to be done and how I"
    " finally mastered the power of infinity. Then I finished my gauntlet and will now rule the universe how I see fit."
    " Good luck. You all have a 50 percent chance to enjoy the utopia that will follow.",
    "I have decided that I would on the growth of artificial intelligence. I want to research whether or not it is a"
    " problem that computers are constantly getting closer to being able to learn and think for themselves. As"
    " computers continue to grow and progress in this way more people have shown concern for what computers are going"
    " to be capable of in the near future. I have always been fascinated by artificial intelligence and what it could"
    " accomplish and can't wait to see what it can become. I hope to one day become an artificial intelligence"
    " specialist and contribute to these advancements so it would be interesting to learn how people working in this"
    " field as well as people in the roll of the consumer who utilize this technology as well.\n"
    "I should find out what truly separates machines with machine-learning and artificial intelligence from any other "
    "computer reliant machines. I should also look into what are the potential problems to arise from this as well as "
    "what could be the potential benefits. There are many who are worried about this from a job standpoint. It would be"
    " important to look into what kinds of jobs would be more affected than others as well as how the progress of"
    " artificial intelligence could affect the availability of jobs. Another important thing to look into is how"
    " plausible are people's main concerns when it comes to the increasing progress in artificial intelligence. Does"
    " our dependency on technology and personal ineptitude for day to day things increase as computers become better"
    " at performing these tasks for us? What are the most advanced systems capable of today and is it plausible that"
    " they could expand into other areas of expertise on their own? ",
    "Nullam non laoreet sem. Nullam non consectetur augue. Integer congue venenatis tellus id vehicula. Cras eleifend"
    " dignissim sapien. Sed ut diam at eros congue feugiat. In lorem lacus, congue eu posuere in, ullamcorper sed"
    " turpis. Ut vel ligula sed erat finibus ultrices quis eget mauris. Pellentesque imperdiet sagittis lacus vel"
    " euismod. Nullam urna justo, tempor sit amet nulla quis, venenatis eleifend quam. Donec imperdiet tincidunt mi"
    " eget hendrerit. Donec mattis enim in eros accumsan consequat. Mauris rhoncus lorem vitae elit iaculis, eu dapibus"
    " nulla efficitur. Praesent porttitor ullamcorper est, quis semper elit hendrerit vitae. Curabitur tempus magna "
    "tellus, imperdiet elementum nisl elementum non. Vestibulum nec felis at tortor ultrices consectetur. Fusce "
    "ultrices tempus magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."
    " Donec et imperdiet tellus. Maecenas blandit rhoncus augue, finibus ornare nibh fermentum et. Nulla et sapien quis"
    " eros consectetur gravida. Phasellus sit amet urna quis nibh scelerisque ornare. Sed et semper quam. Aliquam nunc"
    " orci, porta vitae scelerisque id, ornare eget mauris. Pellentesque tincidunt molestie est et egestas. Nam ac "
    "felis eu ligula elementum efficitur. Curabitur id nisl viverra, tristique dolor quis, vestibulum eros. Suspendisse"
    " in feugiat ex. Mauris quam nisi, sollicitudin at nibh nec, pellentesque ultricies odio. Vivamus metus felis, "
    "dignissim volutpat urna vel, euismod consequat leo. Ut tincidunt risus sit amet elementum varius.Cras rhoncus "
    "convallis tempus. Etiam non iaculis nuncCras rhoncus convallis tempus. Etiam non iaculis nunc Cras rhoncus "
    "convallis tempus. Etiam non iaculis nuncCras rhoncus convallis tempus. Etiam non iaculis nunc"]

filler_names = ["Groghdns Ddong", "Vivamus Tempus", "Orci Varius",  "Jungki Cdhtine"]
filler_emails = ["kfgdfgkadjgn@example.com", "dfdsffgadoih@example.com", "djgkjdfga4341@example.com",
                 "dfhdah47665793@example.com"]
filler_titles = ["What is a Hero?", "Interesting Day", "Research Topic", "Adodfngit"]
filler_commments = ["Etiam convallis nec ligula non iaculis. Morbi id justo at nunc feugiat rhoncus. Fusce nisl orci,"
                    " sollicitudin a turpis id, efficitur tempor eros. In ultrices erat fringilla tellus faucibus, eget"
                    " tincidunt magna fringilla. Duis ut lectus mauris. Vivamus egestas ipsum lorem, vitae sollicitudin"
                    " nisl porttitor eu. Vestibulum et vulputate augue. Nunc congue erat vel porttitor ullamcorper."
                    " Nam rhoncus tortor neque, eu molestie metus gravida quis. Cras rhoncus convallis tempus. Etiam "
                    "non iaculis nunc.",
                    " Mauris quam nisi, sollicitudin at nibh nec, pellentesque ultricies odio. Vivamus metus felis,"
                    " dignissim volutpat urna vel, euismod consequat leo. Ut tincidunt risus sit amet elementum"
                    " varius.",
                    "Cras rhoncus convallis tempus. Etiam non iaculis nunc.",
                    "Donec massa metus, pulvinar id nunc a, ornare maximus lectus. Etiam nec gravida lacus. Praesent"
                    " faucibus arcu vitae mollis ultrices. Quisque eget elit auctor, varius enim vitae, lacinia nisi."]


def home(request):  # home view
    latest_post_list = Blog.objects.order_by("-post_date")[:5]
    template = loader.get_template('blog/home.html')
    context = {'latest_post_list': latest_post_list, }
    return HttpResponse(template.render(context, request))


def archive(request):
    latest_post_list = Blog.objects.order_by("-post_date")
    template = loader.get_template('blog/archive.html')
    context = {'latest_post_list': latest_post_list}
    return HttpResponse(template.render(context, request))


def entry(request, question_id):  # detail view
    try:
        blog = Blog.objects.get(pk=question_id)
    except Blog.DoesNotExist:
        raise Http404("Blog post does not exist")
    return render(request, 'blog/entry.html', {'blog': blog})


def add_comment(request, question_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=question_id)
        c = Comment(blog_id=blog, comment_content=request.POST['Comment'],
                    username=request.POST['Username'], email=request.POST['EmailAddress'])
        c.save()
        return render(request, 'blog/entry.html', {'blog': blog})


def index(request):
    return render(request, 'blog/index.html', {'now': strftime('%c')})


def init(request):
    # deleting all of the blog posts and their associated comments
    Blog.objects.all().delete()
    for i in range(0, 4):
        b = Blog(post_content=filler[i], author=filler_names[i], title=filler_titles[i])
        b.save()
        for j in range(0, 4):
            c = b.comment_set.create(comment_content=filler_commments[j], username=filler_names[j], email=filler_emails[j])
            c.save()
    return render(request, 'blog/index.html', {'now': strftime('%c')})


def Bio(request):
    return render(request, 'blog/Bio.html',
                  {'now': strftime('%c')})


def TecTips(request):
    return render(request, 'blog/TecTips.html',
                  {'now': strftime('%c')})
