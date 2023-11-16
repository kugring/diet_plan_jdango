from uuid import uuid4

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
import os
from Jinstagram.settings import MEDIA_ROOT
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import get_object_or_404  # 데이터를 조회하다가 값이 없는 경우 오류를 반환합니다


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        return render(request, 'jinstagram/main.html', context=dict(feeds=feed_list))


class Date_feed_send(APIView):
    def get(selfself, request):

        today = datetime.today().date()
        image_data_아침 = Feed.objects.filter(upload_date=today, tag='아침').first()

        context = {'img_feed_아침': image_data_아침}

        return render(request, 'jinstagram/kugring.html', context)


class Kugring(APIView):
    def get(self, request):

        today = datetime.today().date()
        image_data_아침 = Feed.objects.filter(upload_date=today, tag='아침').first()
        image_data_점심 = Feed.objects.filter(upload_date=today, tag='점심').first()
        image_data_저녁 = Feed.objects.filter(upload_date=today, tag='저녁').first()
        image_data_기타1 = Feed.objects.filter(upload_date=today, tag='기타1').first()
        image_data_기타2= Feed.objects.filter(upload_date=today, tag='기타2').first()

        image_data_유산소 = Feed.objects.filter(upload_date=today, tag='유산소').first()
        image_data_웨이트 = Feed.objects.filter(upload_date=today, tag='웨이트').first()
        image_data_만보기 = Feed.objects.filter(upload_date=today, tag='만보기').first()
        image_data_눈캠 = Feed.objects.filter(upload_date=today, tag='눈캠').first()
        image_data_크로키 = Feed.objects.filter(upload_date=today, tag='크로키').first()




        main_clr = 'rgb(255,202,136)'
        sub_clr = 'rgb(255,165,63)'
        pastel_clr = ['rgb(255,214,214)',
                      'rgb(255,231,197)',
                      'rgb(216,248,189)',
                      'rgb(193,200,255)']
        h_pastal_clr = ['rgba(241,67,67,0.8)',
                        'rgb(255,162,68)',
                        'rgba(85,199,59,0.9)',
                        'rgba(83,64,255,0.7)']
        nav_title = ['diet', 'exercise', 'morning_record', 'evening_record']
        diet = ["아침", "점심", "저녁", "기타1", "기타2"]
        exercise = ["유산소", "웨이트", "만보기", "눈캠", "크로키"]
        morning_record = ['체중', '허리둘레', '수면시간', '수면만족도', '근육통', '구내염']
        evening_record = ['식사균형', '식사시간', '스트레스', '피로감', '소화불량', '불면증']
        plan_chart = ['diet_chart', 'kcal_chart', 'condition_chart']
        test = [image_data_아침, image_data_점심, image_data_저녁, image_data_기타1, image_data_기타2, image_data_유산소, image_data_웨이트, image_data_만보기, image_data_눈캠, image_data_크로키]
        plan_context = {
            'pastel_clr': pastel_clr,
            'h_pastel_clr': h_pastal_clr,
            'nav_title': nav_title,
            'diet': diet,
            'main_clr': main_clr,
            'sub_clr': sub_clr,
            'exercise': exercise,
            'morning_record': morning_record,
            'evening_record': evening_record,


            'image_data_아침': image_data_아침,
            'image_data_점심': image_data_점심,
            'image_data_저녁': image_data_저녁,
            'image_data_기타1': image_data_기타1,
            'image_data_기타2': image_data_기타2,

            'image_data_유산소': image_data_유산소,
            'image_data_웨이트': image_data_웨이트,
            'image_data_만보기': image_data_만보기,
            'image_data_눈캠': image_data_눈캠,
            'image_data_크로키': image_data_크로키,

            'plan_chart': plan_chart,
            'test': test
        }

        return render(request, 'jinstagram/kugring.html', plan_context)


class UploadFeed(APIView):
    def post(self, request):
        tag = request.data.get('tag')
        upload_date = request.data.get('upload_date')

        # 이미 존재하는 데이터를 찾아보고, 중복 데이터가 없을 때 새로운 데이터를 추가하거나 업데이트
        existing_feed = Feed.objects.filter(tag=tag, upload_date=upload_date).first()

        if existing_feed:
            # 이미 존재하는 데이터가 있을 경우 업데이트
            number_data = request.data.get('number_data')
            user_id = request.data.get('user_id')
            created_at = request.data.get('created_at')

            # 업데이트할 필드를 업데이트하고 저장
            file = request.FILES.get('file')
            uuid_name = uuid4().hex
            save_path = os.path.join(MEDIA_ROOT, uuid_name)

            with open(save_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            existing_feed.image = uuid_name  # 이미지 업데이트
            existing_feed.number_data = number_data
            existing_feed.user_id = user_id
            existing_feed.save()

        else:
            # 중복 데이터가 없을 경우 새로운 데이터 추가
            file = request.FILES.get('file')
            uuid_name = uuid4().hex
            save_path = os.path.join(MEDIA_ROOT, uuid_name)

            with open(save_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            image = uuid_name
            number_data = request.data.get('number_data')
            user_id = request.data.get('user_id')
            created_at = request.data.get('created_at')

            Feed.objects.create(image=image, number_data=number_data, user_id=user_id,
                                tag=tag, like_count=0, created_at=created_at,
                                upload_date=upload_date)

        return Response(status=200)


class Check_duplicate(APIView):
    def get(self, request):
        upload_date = request.GET.get('upload_date', None)
        tag = request.GET.get('tag', None)

        # 이미지 업로드 날짜와 태그를 기반으로 중복 여부를 확인
        is_duplicate = Feed.objects.filter(upload_date=upload_date, tag=tag).exists()

        response_data = {'is_duplicate': is_duplicate}
        return JsonResponse(response_data)
