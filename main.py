import flet as ft
import requests
import asyncio
import os,sys


if getattr(sys, "frozen", False):
    ASSET_YOLU = os.path.join(sys._MEIPASS, "assets")

else:
    ASSET_YOLU = "assets"

async def main(pencere: ft.Page):
    pencere.title = "Pear- İstek Kutusu"
    pencere.vertical_alignment = ft.MainAxisAlignment.CENTER
    pencere.horizontal_alignment = ft.CrossAxisAlignment.CENTER




    pencere.add(ft.Image(src="Pear-Animation.gif", width=250, height=250))

    await asyncio.sleep(1.7)

    pencere.clean()

    def gonder(e):
        URL = "https://ntfy.sh/pear_os_sinif_istekleri_025"
        ad = yaziad.value
        anlatim = yazitanitim.value
        platform = yaziplatform.value


        if not ad or not ad.strip() or not anlatim or not anlatim.strip() or not platform or not platform.strip():
            yazi.value = "Lütfen Her Alanı Doldurunuz \n"
            pencere.update()
            return
        else:
            yazi.value = "Talebiniz Uygulanmıştır, Habat size dediğinde uygulama hazırdır"

        hazir_metin = f"Ad: {ad}, Uygulaması: {anlatim}, platform: {platform}"

        try:
            requests.post(URL, data=hazir_metin.encode("utf-8"))

        except:
            yazi.value = "İnternet Kopuk Veya Baka Bir Şey Oldu, Lütfen Tekrar Deneyin"



        pencere.update()


    yaziad = ft.TextField(label="Lütfen Adınızı Gİrin")

    yazitanitim = ft.TextField(label="Uygulamanızın Anlatımı", multiline=True)

    yaziplatform = ft.Dropdown(label="Platform",
        options=[
        ft.dropdown.Option("Mobil"),
        ft.dropdown.Option("Pc(Bilgisayar)"),
        ft.dropdown.Option("Çapraz Platform(Hem pc, hem mobil)")
        ]
        )

    buton = ft.Button("Gönder", width=100, height=75, on_click=gonder)

    yazi = ft.Text("", size=20)

    pencere.add(yaziad, yazitanitim, yaziplatform, buton, yazi)

ft.run(main, assets_dir=ASSET_YOLU)
