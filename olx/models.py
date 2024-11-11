from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from django.utils.safestring import mark_safe

class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=50)
    keyword = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    slug = models.SlugField(blank=True, null=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def full_path(self):
        return " > ".join([ancestor.title for ancestor in self.get_ancestors(include_self=True)])

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'


class Product(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),
    )

    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    minamount = models.PositiveIntegerField(default=3)
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    detail = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    parent = models.PositiveIntegerField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""


class Size(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)

    def __str__(self):
        return self.name

class Variants(models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    image_id = models.IntegerField(blank=True,null=True,default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,blank=True,null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title

    def image(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
             varimage=img.image.url
        else:
            varimage=""
        return varimage

    def image_tag(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
             return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""

class Jobs(models.Model):
    JOB_TYPES = [('remote', 1), ('office', 2)]
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='office')
    posted_on = models.DateField()
    location = models.CharField(max_length=50)


















# class Category(models.Model):
#     category_name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=200, blank=True, null=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.category_name)
#         super(Category, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.category_name
#
#     class Meta:
#         verbose_name = 'category'
#         verbose_name_plural = 'Categories'
#
# class QuantityVariant(models.Model):
#     quantity_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.quantity_name
#
#     class Meta:
#         verbose_name = 'quantity variant'
#         verbose_name_plural = 'Quantity variants'
#
# class ColorVariant(models.Model):
#     color_name = models.CharField(max_length=100)
#     color_code = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.color_name
#
#     class Meta:
#         verbose_name = 'color'
#         verbose_name_plural = 'Colors'
#
# class SizeVariant(models.Model):
#     size_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.size_name
#
#     class Meta:
#         verbose_name = 'size'
#         verbose_name_plural = 'Sizes'
#
# class Product(models.Model):
#     product_name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='products_image/')
#     price = models.DecimalField(max_digits=12, decimal_places=2)
#     description = models.TextField()
#     stock = models.IntegerField(default=100)
#
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     quantity_type = models.ForeignKey(QuantityVariant, on_delete=models.CASCADE, blank=True, null=True)
#     color_type = models.ForeignKey(ColorVariant, on_delete=models.CASCADE, blank=True, null=True)
#     size_type = models.ForeignKey(SizeVariant, on_delete=models.CASCADE, blank=True, null=True)
#
#     def __str__(self):
#         return self.product_name
#
#     class Meta:
#         verbose_name = 'product'
#         verbose_name_plural = 'Products'
