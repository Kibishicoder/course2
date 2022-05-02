#
#
# response = app.test_client().get('/api/posts', follow_redirects=True)
# А там уже делаем ассерты, например
# assert response.status_code == 200, "Статус код запроса всех постов неверный"