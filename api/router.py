from fastapi import APIRouter

from api.schemas import FibResponse
from rpc.client import FibRpcClient

fib_rpc = FibRpcClient()
router = APIRouter(prefix="/fib", tags="fib")


@router.post("/{number}", response_model=FibResponse)
def calculate_fibonacci(number: int):
    print(f"[x] Requesting fib({number})")
    result = fib_rpc.call(number)
    print(f"[.] Got {result}")
    return {
        "fibonacci": result,
        "number": number,
    }
