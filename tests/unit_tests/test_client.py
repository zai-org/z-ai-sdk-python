def test_completions_image_url_data_image(monkeypatch):
    from zai import ZaiClient
    client = ZaiClient()
    # 构造 messages，包含 image_url 且 url 以 data:image/ 开头
    base64_str = 'abc123=='
    messages = [
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'What is in this image?'},
                {'type': 'image_url', 'image_url': {'url': f'data:image/png;base64,{base64_str}'}},
            ]
        }
    ]
    # mock client.post 方法只返回 body 以便断言
    def fake_post(*args, **kwargs):
        return kwargs.get('body', {})
    monkeypatch.setattr(client, 'post', fake_post)
    result = client.chat.completions.create(model='glm-4', messages=messages)
    # 验证 image_url 的 url 字段已去除前缀
    content = result['messages'][0]['content']
    image_url = [x for x in content if x.get('type') == 'image_url'][0]
    assert image_url['image_url']['url'] == base64_str