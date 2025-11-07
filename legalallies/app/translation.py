from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Article, ComplementaryMaterial, SocialNetwork, HomeConfiguration


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


class ComplementaryMaterialTranslationOptions(TranslationOptions):
    fields = ('body',)


class SocialNetworkTranslationOptions(TranslationOptions):
    fields = ('name',)


class HomeConfigurationTranslationOptions(TranslationOptions):
    fields = ('banner_title', 'banner_description', 'card1_title', 'card1_description', 'card2_title', 'card2_description')


translator.register(Category, CategoryTranslationOptions)
translator.register(Article, ArticleTranslationOptions)
translator.register(ComplementaryMaterial, ComplementaryMaterialTranslationOptions)
translator.register(SocialNetwork, SocialNetworkTranslationOptions)
translator.register(HomeConfiguration, HomeConfigurationTranslationOptions)
