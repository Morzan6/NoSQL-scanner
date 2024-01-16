from pydantic import BaseModel, Field

class UserLoginSerializer(BaseModel):
        """Data serializer for user login"""
        username: str = Field(pattern=r"^[A-Za-z0-9_@!]+$", max_length=100)
        password: str = Field(min_length=8)
        

class TokenSerializer(BaseModel):
        """Data serializer for JWT token"""
        access_token: str
        
class ScanStartSerializer(BaseModel):
        """Data serializer for start new scan"""
        name: str = Field(max_length=20, pattern=r'^[\p{Cyrillic}.(),:;A-Za-z0-9]+$')
        description: str = Field(max_length=15)
        ip: str = Field(pattern=r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')
        port: int = Field(le=65535, gt=0)
