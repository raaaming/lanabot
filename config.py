'''
    <config.py>
    봇의 설정을 이렇게 따로 빼 놓으면 편하게 설정할 수 있어요!
    - 키뮤 제작(0127 버전)
'''


class Config:
    # 봇의 토큰을 넣어 주세요
    token = 'ODQxNzM5OTUxMDQwODg4ODQ0.YJrJaw.zdp0lX9U-Y60zXM1WnB4j1Gb5V4'
    # 디버그 모드가 켜졌을 때 사용할 토큰을 넣어주세요(위와 똑같이 넣어도 괜찮아요)
    test_token = 'ODQxNzM5OTUxMDQwODg4ODQ0.YJrJaw.zdp0lX9U-Y60zXM1WnB4j1Gb5V4'

    # 디버그 여부
    is_debug = False

    # 하고 있는 게임 (프로필에 '... 하는 중'으로 보이는 것)
    activity = "라나가 테스트 중이라고 말"

    # 접두사(명령어 앞에 붙여야 하는 것)
    # '~야' 같이 뒤의 명령어와 띄어서 써야 하는 접두사는 뒤를 한 칸 띄어 주세요! (예시의 '세타야 ')
    # 접두사는 여러 개를 지정할 수 있어요.
    prefixes = ['l/', '라나야 ']

    # 봇의 버전을 입력해 주세요. 테스트 명령어에서 쓴답니다.
    version = '1.0'

    # 관리자 디스코드 id 목록
    admin = [734023826559729734]

    def using_token(self):
        '''
        사용해야 하는 봇 토큰을 반환합니다.
        '''
        if self.is_debug:
            return self.test_token
        else:
            return self.token

    def prefixes_no_space(self):
        '''
        접두사들을 띄어쓰기 없이 반환합니다.
        '''
        result = []
        for i in self.prefixes:
            result.append(i.replace(' ', ''))
        return result
