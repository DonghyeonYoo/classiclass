from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.utils.sms import send_sms

from posts.models import Post
from tags.models import Tag
from users.models import User


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if not instance.hash_id:
        instance.init_hash_id()


@receiver(post_save, sender=Post)
def post_save_post_tags(sender, instance, created, **kwargs):
    tag_list = [
        word.replace("#", "")
        for word
        in instance.content.split(" ")
        if word.startswith("#")
    ]

    for tag_name in tag_list:
        tag, is_tag_created = Tag.objects.get_or_create(
            name=tag_name,
        )
        instance.tag_set.add(tag)

# 포스트가 생기면 유저매칭을 시작하겠다는함수
# 매개변수로 모델을 받고 생성된 인스턴스 옛날에 생성됬는데 update만된건지 방금생성된건지


@receiver(post_save, sender=Post)
def post_save_post_and_user_is_matched(sender, instance, created, **kwargs):

    if created:
        post_tag = instance.tag_set.all()
        post_tag_list = instance.tag_set.values_list('name', flat=True)
        user_major_of_post = User.objects.filter(majors__in=post_tag_list)
        user_age_of_post = User.objects.filter(ages__in=post_tag_list)
        user_data_of_posts = list(user_major_of_post) + list(user_age_of_post)
        phonenumber_list = []
        for user_data_of_post in user_data_of_posts:
            phonenumber_list.append(
                user_data_of_post.phonenumber
            )
# post_save.connect(post_save_post_and_user_is_matched, sender=Post)
        for phonenumber in phonenumber_list:
            send_sms(
                "01091777233",
                phonenumber,
                "{USERNAME} 님과 매칭되는 콩쿠르 정보=({POSTNAME})가 업로드 되었습니다".format(
                    USERNAME=User.objects.get(phonenumber=phonenumber).username,
                    POSTNAME=instance.title,
                )
            )
