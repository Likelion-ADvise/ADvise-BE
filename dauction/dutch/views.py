import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Ad, Proposal

def create_ad(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        content = data.get('content')
        minimum_price = data.get('minimum_price')

        ad = Ad(
            title=title,
            content=content,
            minimum_price=minimum_price
        )
        ad.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'POST 요청만 허용됩니다.'}, status=400)

def create_proposal(request, ad_id):
    if request.method == 'POST':
        data = json.loads(request.body)

        ad = get_object_or_404(Ad, id=ad_id)
        identifier = data.get('identifier')
        pwd = data.get('pwd')
        name = data.get('name')
        url = data.get('url')
        info = data.get('info')
        price = data.get('price')

        proposal = Proposal(
            ad=ad,
            identifier=identifier,
            pwd=pwd,
            name=name,
            url=url,
            info=info,
            price=price
        )
        proposal.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'POST 요청만 허용됩니다.'}, status=400)

def get_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    data = {
        'id': ad.pk,
        'title': ad.title,
        'content': ad.content,
        'minimum_price': ad.minimum_price,
        'created_at': ad.created_at
    }
    return JsonResponse(data, status=200)

def delete_proposal(request, ad_id, pk):
    if request.method == 'DELETE':
        proposal = get_object_or_404(Proposal, pk=pk, ad_id=ad_id)
        data = json.loads(request.body)
        if proposal.pwd == data.get('pwd'):
            proposal.delete()
            return JsonResponse({'message': f'id: {pk} 제안 삭제 완료'}, status=200)
        else:
            return JsonResponse({'message': '비밀번호가 일치하지 않습니다.'}, status=403)
    return JsonResponse({'message': 'DELETE 요청만 허용됩니다.'}, status=400)

def get_all_ads(request):
    if request.method == 'GET':
        ads = Ad.objects.all()
        ads_data = [
            {
                'id': ad.id,
                'title': ad.title,
                'content': ad.content,
                'minimum_price': ad.minimum_price
            }
            for ad in ads
        ]
        return JsonResponse(ads_data, safe=False)
    return JsonResponse({'message': 'GET 요청만 허용됩니다.'})

