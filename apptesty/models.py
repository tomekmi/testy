# -*- coding: utf-8 -*-
from django.db import models

class Tests(models.Model):
    name = models.CharField(max_length=256, verbose_name="Nazwa testu")
    description = models.CharField(max_length=512, verbose_name="Krótki opis")

    def __unicode__(self):
        return self.name 
    class Meta:
         verbose_name = "Test"
         verbose_name_plural = "Testy"
         
class Questions(models.Model):
    test = models.ForeignKey(Tests)
    question = models.CharField(max_length=512, verbose_name="Pytanie")

    def __unicode__(self):
        return self.question
    class Meta:
         verbose_name = "Pytanie"
         verbose_name_plural = "Pytania"
         
class Answers(models.Model):
    question = models.ForeignKey(Questions)
    answer = models.CharField(max_length=512, verbose_name="Odpowiedź")
    isCorrect = models.BooleanField(verbose_name="Poprawna")

    def __unicode__(self):
        return self.answer
    class Meta:
         verbose_name = "Odpowiedź"
         verbose_name_plural = "Odpowiedzi"
