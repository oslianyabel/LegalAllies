from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    hero_image = models.ImageField(upload_to="categories/hero/")
    image = models.ImageField(upload_to="categories/")
    other_services_image = models.ImageField(
        upload_to="categories/other_services/", blank=True, null=True
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=350, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="articles"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    image = models.ImageField(upload_to="articles/")
    complementary_material_image = models.ImageField(
        upload_to="articles/complementary/", blank=True, null=True
    )
    complementary_material = models.ForeignKey(
        "ComplementaryMaterial",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ComplementaryMaterial(models.Model):
    MATERIAL_TYPES = [
        ("video", "Video"),
        ("document", "Document"),
        ("infographic", "Infographic"),
        ("other", "Other"),
    ]

    type = models.CharField(max_length=50, choices=MATERIAL_TYPES)
    body = RichTextField()
    video = models.URLField(blank=True, null=True)
    pdf = models.FileField(
        upload_to="complementary_materials/pdfs/", blank=True, null=True
    )

    def __str__(self):
        return f"{self.get_type_display()}" # type: ignore


class SocialNetwork(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="social_networks/")
    link = models.URLField()

    def __str__(self):
        return self.name


class HomeConfiguration(models.Model):
    logo = models.ImageField(upload_to="home/logo/")
    main_image = models.ImageField(upload_to="home/main/")
    banner_title = models.CharField(max_length=200)
    banner_description = models.TextField()
    banner_image = models.ImageField(upload_to="home/banner/")
    card1_title = models.CharField(max_length=200)
    card1_description = models.TextField()
    card1_svg = models.FileField(upload_to="home/svgs/")
    card2_title = models.CharField(max_length=200)
    card2_description = models.TextField()
    card2_svg = models.FileField(upload_to="home/svgs/")
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField()
    socialNetwork = models.ManyToManyField(
        SocialNetwork, blank=True, related_name="home_configurations"
    )

    class Meta:
        verbose_name = "Home Configuration"
        verbose_name_plural = "Home Configuration"

    def __str__(self):
        return "Home Configuration"
