from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

# أسعار الباقات
PLAN_PRICES = {
    "Plan1": 100,
    "Plan2": 200,
    "Plan3": 300
}

# شكل البيانات اللي الفورم هيبعتها
class RegistrationForm(BaseModel):
    prefix: str
    name: str
    email: EmailStr
    phone: str
    institution: str
    city: str
    scfhs_no: str
    plan: str

@app.get("/")
def home():
    return {"message": "API is working!"}

@app.post("/register")
def register_user(form: RegistrationForm):
    if form.plan not in PLAN_PRICES:
        raise HTTPException(status_code=400, detail="Invalid plan selected")

    price = PLAN_PRICES[form.plan]

    # ممكن تخزن البيانات في قاعدة بيانات أو تبعتها لإيميل
    print("New Registration:", form.dict())

    return {
        "status": "success",
        "plan": form.plan,
        "price": price,
        "message": "Registration successful"
    }
