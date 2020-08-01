from django.db import models

class Poll(models.Model):
    question=models.TextField()
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option1_counts=models.IntegerField(default=0)
    option2_counts=models.IntegerField(default=0)
    option3_counts=models.IntegerField(default=0)
    
    def total(self):
        return self.option1_counts + self.option2_counts + self.option3_counts
