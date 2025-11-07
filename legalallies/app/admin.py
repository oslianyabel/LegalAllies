from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    Article,
    Category,
    ComplementaryMaterial,
    HomeConfiguration,
    SocialNetwork,
)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ["title", "category", "author", "created_at"]
    list_filter = ["category", "created_at", "author"]
    search_fields = ["title", "body"]
    date_hierarchy = "created_at"
    raw_id_fields = ["author"]
    autocomplete_fields = ["category", "complementary_material"]


@admin.register(ComplementaryMaterial)
class ComplementaryMaterialAdmin(TranslationAdmin):
    list_display = ["type", "get_articles_count"]
    list_filter = ["type"]
    search_fields = ["body"]

    def get_articles_count(self, obj: ComplementaryMaterial) -> int:
        return obj.articles.count() # type: ignore

    get_articles_count.short_description = "Articles"


@admin.register(SocialNetwork)
class SocialNetworkAdmin(TranslationAdmin):
    list_display = ["name", "link"]
    search_fields = ["name"]


@admin.register(HomeConfiguration)
class HomeConfigurationAdmin(TranslationAdmin):
    fieldsets = [
        ("Logo & Main Image", {"fields": ["logo", "main_image"]}),
        ("Banner", {"fields": ["banner_title", "banner_description", "banner_image"]}),
        ("Card 1", {"fields": ["card1_title", "card1_description", "card1_svg"]}),
        ("Card 2", {"fields": ["card2_title", "card2_description", "card2_svg"]}),
        (
            "Contact",
            {
                # include the socialNetwork ManyToMany field so it can be edited via admin
                "fields": ["contact_phone", "contact_email", "socialNetwork"]
            },
        ),
    ]
