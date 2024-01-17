import os

TEST_SECRET = os.environ["test_secret"]
Test_secret = os.getenv("test_secret")

if (TEST_SECRET=="HelloWorld" and Test_secret == "HelloWorld"):
  print(f"The client secret is: {TEST_SECRET}")
  print(f"The client secret 2 is: {Test_secret}"):
elif (TEST_SECRET=="HelloWorld"):
  print(f"The client secret is: {TEST_SECRET}")
elif (Test_secret == "HelloWorld"):
  print(f"The client secret 2 is: {Test_secret}")
else:
  print(f"Test secret doesnt matches")
