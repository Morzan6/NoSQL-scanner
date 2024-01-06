from pydantic import BaseModel, Field

class UserLoginSerializer(BaseModel):
        """Data serializer for user login"""
        username: str = Field(pattern=r"^[A-Za-z0-9_@!]+$", max_length=100)
        password: str = Field(min_length=8)
        

class TokenSerializer(BaseModel):
        """Data serializer for JWT token"""
        access_token: str
        
class ScanStartSerializer(BaseModel):
    ip: str = Field(pattern=r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')
    port: int = Field(max_length=8)