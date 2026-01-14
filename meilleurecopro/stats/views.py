import numpy
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advertisement


BIENICI_BASE_URI = "https://www.bienici.com/realEstateAd.json?id="


class Statistics(APIView):
    def get(self, request) -> Response:
        dept = request.query_params.get("department", None)
        city = request.query_params.get("city", None)
        zipcode = request.query_params.get("zipcode", None)

        if zipcode is None and city is None and dept is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = Advertisement.objects.filter(condominium_fees__isnull=False)
        if zipcode:
            advertisements = (
                queryset.filter(zipcode=zipcode)
                .order_by("condominium_fees")
                .values_list("condominium_fees")
            )
        elif city:
            advertisements = (
                queryset.filter(city=city)
                .order_by("condominium_fees")
                .values_list("condominium_fees")
            )
        elif dept:
            advertisements = (
                queryset.filter(department=dept)
                .order_by("condominium_fees")
                .values_list("condominium_fees")
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if len(advertisements) < 1:
            data = {"error": "No data for your request"}
        else:
            data = {
                "mean": round(numpy.mean(advertisements), 2),
                "q10": round(numpy.percentile(advertisements, 10), 2),
                "q90": round(numpy.percentile(advertisements, 90), 2),
            }
        return Response(data=data, status=status.HTTP_200_OK)


class Advertisements(APIView):
    def post(self, request) -> Response:
        url = request.data.get("url", None)

        if url is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # extract the bienici_id from url
        try:
            bienici_id = url.split("/")[-1]
        except:
            return Response(
                data={"error": "invalid url"}, status=status.HTTP_400_BAD_REQUEST
            )

        response = requests.request("GET", BIENICI_BASE_URI + str(bienici_id))

        if response.status_code != 200:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = response.json()
        Advertisement.objects.update_or_create(
            bienici_id=bienici_id,
            department=data["postalCode"][0:2],
            city=data["city"],
            zipcode=data["postalCode"],
            condominium_fees=float(data["annualCondominiumFees"]),
        )
        return Response(status=status.HTTP_201_CREATED)
