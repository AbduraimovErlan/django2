from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Book_Comment(models.Model):
    post = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    email = models.EmailField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True, null=True)


    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class BookRating(models.Model):
    RATING_CHOICE = (
        ('1 *', '1 *'),
        ('2 **', '2 **'),
        ('3 ***', '3 ***'),
        ('4 ****', '4 ****'),
        ('5 *****', '5 *****')
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_rating")
    rating = models.CharField(choices=RATING_CHOICE, max_length=100)


class Expert(models.Model):
    PERFORMANCE_CHOICE = (
        ('Doctor', 'Doctor'),
        ('Writer', 'Writer'),
        ('Scientist', 'Scientist'),
        ('ACTOR', 'ACTOR'),
        ('Artist', 'Artist'),
    )
    expert = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='expert')
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    performance = models.CharField(choices=PERFORMANCE_CHOICE, max_length=100)
    info = models.TextField()


    def __str__(self):
        return 'Expert {} recommends book {}'.format(self.firstName, self.expert)




class ExpertRecommendation(models.Model):
    bookExpert = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="bookExpert")
    text = models.TextField()
    expertRecommendation = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name="expertRecommendation")
