SIGNUP_POST = {
    'tags': ['계정'],
    'description': '회원가입',
    'parameters': [
        {
            'name': 'id',
            'description': '회원 id',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'password',
            'description': '회원 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '회원 가입 성공'
        },
        '409': {
            'description': '이미 존재 하는 id'
        }
    }
}