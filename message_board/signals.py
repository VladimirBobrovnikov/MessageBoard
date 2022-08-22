from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from message_board.models import Reaction
from SF_Finall.settings import DEFAULT_FROM_EMAIL


@receiver(post_save, sender=Reaction)
def send_mail(sender, instance, created, **kwargs):

    if created:
        user = instance.post.author

        html = render_to_string(
            'message_board/messages/new_reaction.html',
            {
                'user': user,
                'reaction': instance,
             },
        )

        msg = EmailMultiAlternatives(
                subject=f'Вы получили новый отклик!',
                from_email=DEFAULT_FROM_EMAIL,
                to=[user.email]
            )

        msg.attach_alternative(html, 'text/html')
        msg.send()
    else:
        user = instance.author

        html = render_to_string(
            'message_board/messages/update_reaction.html',
            {
                'user': user,
                'reaction': instance,
             },
        )

        msg = EmailMultiAlternatives(
                subject=f'Обновлен статус вашего отклика!',
                from_email=DEFAULT_FROM_EMAIL,
                to=[user.email]
            )

        msg.attach_alternative(html, 'text/html')
        msg.send()
