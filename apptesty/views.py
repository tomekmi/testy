from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from apptesty.models import Tests, Questions, Answers
from django.db.models import Q
import string

def home(request):
    if not request.user.is_authenticated():
        return render_to_response('registration/login.html', { }, context_instance=RequestContext(request))
    else:
        testsList = Tests.objects.all()
        paginator = Paginator(testsList, 20) # show only 20 tests per page
        page = request.GET.get('page')
    	try:
        	pagedTests = paginator.page(page)
    	except PageNotAnInteger:
        	pagedTests = paginator.page(1)
    	except EmptyPage:
        	pagedTests = paginator.page(paginator.num_pages)
 
        return render_to_response('homeLogged.html', {'user': request.user, 'tests' : pagedTests }, context_instance=RequestContext(request))

def solvetest(request, tid):
    chTest=Tests.objects.get(id=tid)
    chQuestions=Questions.objects.filter(test=chTest)
    chAnswers=Answers.objects.filter(question__test=chTest)
    answers = { }
    for answer in chAnswers:
      if not answers.has_key(answer.question.id):
	 answers[answer.question.id]=[ answer, ]
      else:
         answers[answer.question.id].append(answer)
    return render_to_response('solveTest.html', { 'test' : chTest, 'questions' : chQuestions, 'answers' : answers }, context_instance=RequestContext(request))

def getAnswersDict(param, name):
    dictArr = { }
    for key in param.keys():
      if key.startswith(name):
	indexes = key[len(name):]
	strDec = string.split(indexes, '|')
	try:
	    qNumber = int(strDec[0])
	    qAnswer = int(strDec[1])
	except IndexError:
	    return dictArr
	if not dictArr.has_key(qNumber):
	  dictArr[qNumber] = [ qAnswer, ]
	else:
	  dictArr[qNumber].append(qAnswer)
    return dictArr
	  
def solvetestcheck(request, tid):
    chTest=Tests.objects.get(id=tid)
    chQuestions=Questions.objects.filter(test=chTest)
    chAnswers=Answers.objects.filter(question__test=chTest)
    
    result = 0
    maxResult = chQuestions.count()
    
    #userAnswersFromForm = request.POST.getlist('anwers')
    
    # create dict with user answers:  
    userAnswers = getAnswersDict(request.POST, 'answers')
    correctQuestions = { }
    for question in chQuestions:
      correctQuestions[question.id]=True
      
    for answer in chAnswers: 
      if answer.isCorrect:
	 if not userAnswers.has_key(answer.question.id):
	   correctQuestions[answer.question.id] = False
	 else:
	   if not answer.id in userAnswers[answer.question.id]:
	     correctQuestions[answer.question.id] = False
      else:
	 if userAnswers.has_key(answer.question.id):
	   if answer.id in userAnswers[answer.question.id]:
	     correctQuestions[answer.question.id] = False	
        
    for question in chQuestions:
      if correctQuestions[question.id] == True:
	result+=1
    
    resultPercent = float(result)/float(maxResult)*100.0
      
    mailText=render_to_string('testResultEmail.html', { 'user' : request.user, 'test' : chTest, 'testResult' : result, 'testMaxResult' : maxResult, 'testResultPercent' : resultPercent }) #'Nowe haslo do Twojego konta: '+newPassword

    subject = "Twoj wynik testu"
    from_email =  'tomasz.michno@gmail.com'
    to = request.user.email
    text_content = mailText
    html_content = mailText
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.content_subtype = "html" 
    msg.send()  
      
    return render_to_response('solveTestResults.html', { 'test' : chTest, 'testResult' : result, 'testMaxResult' : maxResult, 'testResultPercent' : resultPercent }, context_instance=RequestContext(request))
  