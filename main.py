from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import stripe
import os

app = FastAPI()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.get("/")
def root():
    return {"message": "Welcome to IProFactory SaaS Backend!"}

@app.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": "IProFactory Pro Plan",
                    },
                    "unit_amount": 1500,
                },
                "quantity": 1,
            }],
            mode="subscription",
            success_url="https://yourdomain.com/success",
            cancel_url="https://yourdomain.com/cancel",
        )
        return {"id": session.id}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
