import httpx

class IngestionClient:
    """
    Bridge between ExamVerse API and Ingestion Engine
    (future microservice or internal module)
    """

    def __init__(self, base_url: str = "http://localhost:9000"):
        self.base_url = base_url

    async def fetch_syllabus(self, exam_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/syllabus/{exam_id}"
            )
            return response.json()

    async def fetch_pyqs(self, exam_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/pyqs/{exam_id}"
            )
            return response.json()

    async def sync_exam_data(self, exam_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/sync/{exam_id}"
            )
            return response.json()