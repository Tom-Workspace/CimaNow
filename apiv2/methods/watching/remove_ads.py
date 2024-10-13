import apiv2


class RemoveAds:
    def remove_ads(client: "apiv2.Client"):
        try:
            client.execute_script(
                """
                var ads = document.querySelectorAll('#xqeqjp, #xqeqjp1');
                ads.forEach(ad => ad.remove());
            """
            )
        except Exception as e:
            print(f"Error while removing ads: {e}")
