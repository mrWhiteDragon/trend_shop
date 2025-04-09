from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, verbose_name='Акционный товар')
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('products:product_detail', args=[self.id, self.slug])