import boto3
import json
import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv

def get_production_config(secret_name: str = "dev/virtuall-monorepo/env", region_name: str = "eu-west-1") -> Dict[str, str]:
    """
    Retrieves production configuration secrets from AWS Secrets Manager.
    Mirrors the logic in the Virtuall platform's getConfig().
    """
    # Load local environment variables if present
    load_dotenv('.env.local')
    
    print(f"DEBUG: AWS_ACCESS_KEY_ID={os.getenv('AWS_ACCESS_KEY_ID')[:4] if os.getenv('AWS_ACCESS_KEY_ID') else 'NONE'}")
    print(f"DEBUG: AWS_SESSION_TOKEN_PRESENT={bool(os.getenv('AWS_SESSION_TOKEN'))}")
    
    print(f"--- Secret Manager: Retrieving secret '{secret_name}' from {region_name} ---")
    
    # We rely on environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN)
    # which Boto3 picks up automatically.
    
    try:
        client = boto3.client(
            service_name='secretsmanager',
            region_name=region_name
        )
        
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            config = json.loads(secret)
            return config
        else:
            print("Warning: Secret found but SecretString is missing.")
            return {}
            
    except Exception as e:
        print(f"Error retrieving AWS Secret: {str(e)}")
        return {}

def bootstrap_production_env(secret_name: str = "dev/virtuall-monorepo/env"):
    """
    Fetches the secrets and injects them into the os.environ.
    """
    config = get_production_config(secret_name)
    if config:
        print(f"--- Secret Manager: Successfully injected {len(config)} keys into environment ---")
        for key, value in config.items():
            if value:
                os.environ[key] = str(value)
        return True
    return False

if __name__ == "__main__":
    # Test execution
    config = get_production_config()
    if config:
        print("Success! Keys found (redacted):")
        for k in config.keys():
            print(f" - {k}")
    else:
        print("Failed to retrieve config.")
