from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentiation(SessionAuthentication):
    def enforce_csrf(self,request):        
        pass   
