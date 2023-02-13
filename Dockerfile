FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

WORKDIR /work

RUN pip install --no-cache-dir --upgrade 3DVG

CMD ["uvicorn", "3DVG:app", "--host", "0.0.0.0", "--port", "80", "--root-path", "/3DVG"]
