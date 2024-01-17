import os

TEST_SECRET = os.environ["test_secret"]
Test_secret = os.getenv("test_secret")

print(f"The client secret is: {TEST_SECRET}")
print(f"The client secret 2 is: {Test_secret}")
