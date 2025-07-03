from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from IproFactory"}

# ✅ Stripe webhook endpoint
@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    print("✅ Stripe webhook received:", payload)
    return {"status": "success"}

# 🚀 Optional local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
