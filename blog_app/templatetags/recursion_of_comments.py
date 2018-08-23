from django import template

from blog_app.models import Comment


register = template.Library()


@register.filter
def get_discus_for_comment(id_article, id_comment):
    """ recursive search id comments """
    discus_id_list = list()  # result id list - for easier calculations
    discus_obj_list = list() # list with Comment obj

    all_comments_by_article_obj = Comment.objects.filter(article=id_article).order_by('create')
    adjacent_list = list(zip(
        list(
            all_comments_by_article_obj.values_list('reply_to_comment', flat=1).filter(reply_to_comment__isnull=False)),
        list(all_comments_by_article_obj.values_list('id', flat=1).filter(reply_to_comment__isnull=False))
    ))

    def dfs(comment_id):
        for i in adjacent_list:
            if (comment_id in i) and (i[1] not in discus_id_list):
                discus_id_list.append(i[1])

                discus = Comment.objects.get(id=i[1])
                discus_obj_list.append(discus)

                dfs(i[1])

    dfs(id_comment)

    if len(discus_id_list) == 0:
        return None
    else:
        # return discus_id_list
        return discus_obj_list
