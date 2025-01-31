import json
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Ad, Proposal
from rest_framework.decorators import api_view

# 게시물 작성
@api_view(['POST'])
def create_ad(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data'))  # form-data에서 데이터를 가져옵니다.
        
        title = data.get('title')
        content = data.get('content')
        minimum_price = data.get('minimum_price')
        image = request.FILES.get('image')  # 파일 데이터를 가져옵니다.

        ad = Ad(
            title=title,
            content=content,
            minimum_price=minimum_price,
            image=image
        )
        ad.save()
        return Response({'message': 'success'})
    return Response({'message': 'POST 요청만 허용됩니다.'}, status=400)

# 특정 한 게시물 가져오기
@api_view(['GET'])
def get_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    data = {
        'id': ad.pk,
        'title': ad.title,
        'content': ad.content,
        'minimum_price': ad.minimum_price,
        'created_at': ad.created_at,
        'image_url': request.build_absolute_uri(ad.image.url) if ad.image else None
    }
    return Response(data, status=200)

# 게시물 전체 조회
@api_view(['GET'])
def get_all_ads(request):
    if request.method == 'GET':
        ads = Ad.objects.all()
        ads_data = [
            {
                'id': ad.id,
                'title': ad.title,
                'content': ad.content,
                'minimum_price': ad.minimum_price,
                'image_url': request.build_absolute_uri(ad.image.url) if ad.image else None
            }
            for ad in ads
        ]
        return Response(ads_data)
    return Response({'message': 'GET 요청만 허용됩니다.'})
#
# 검색어로 게시물 조회 (검색 기능)
@api_view(['GET'])
def search_ads(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        ads = Ad.objects.filter(title__icontains=query)
        ads_data = [
            {
                'id': ad.id,
                'title': ad.title,
                'content': ad.content,
                'minimum_price': ad.minimum_price,
                'image': ad.image
            }
            for ad in ads
        ]
        return Response(ads_data)
    return Response({'message': 'GET 요청만 허용됩니다.'})

# 댓글 작성
@api_view(['POST'])
def create_proposal(request, ad_id):
    if request.method == 'POST':
        data = json.loads(request.body)

        ad = get_object_or_404(Ad, id=ad_id)
        identifier = data.get('identifier')
        pwd = data.get('pwd')
        title = data.get('title')
        url = data.get('url')
        info = data.get('info')
        price = data.get('price')

        proposal = Proposal(
            ad=ad,
            identifier=identifier,
            pwd=pwd,
            title=title,
            url=url,
            info=info,
            price=price
        )
        proposal.save()
        return Response({'message': 'success'})
    return Response({'message': 'POST 요청만 허용됩니다.'}, status=400)

# 댓글 가져오기

# 광고의 모든 댓글 조회
@api_view(['GET'])
def get_all_proposals(request, ad_id):
    if request.method == 'GET':
        ad = get_object_or_404(Ad, id=ad_id)
        proposals = Proposal.objects.filter(ad=ad)
        proposals_data = [
            {
                'id': proposal.id,
                'identifier': proposal.identifier,
                'title': proposal.title,
                'url': proposal.url,
                'info': proposal.info,
                'price': proposal.price,
                'created_at': proposal.created_at
            }
            for proposal in proposals
        ]
        return Response(proposals_data)
    return Response({'message': 'GET 요청만 허용됩니다.'}, status=400)
# 댓글 삭제

@api_view(['DELETE'])
def delete_proposal(request, ad_id, pk):
    if request.method == 'DELETE':
        proposal = get_object_or_404(Proposal, pk=pk, ad_id=ad_id)
        data = json.loads(request.body)
        if proposal.pwd == data.get('pwd'):
            proposal.delete()
            return Response({'message': f'id: {pk} 제안 삭제 완료'}, status=200)
        else:
            return Response({'message': '비밀번호가 일치하지 않습니다.'}, status=403)
    return Response({'message': 'DELETE 요청만 허용됩니다.'}, status=400)