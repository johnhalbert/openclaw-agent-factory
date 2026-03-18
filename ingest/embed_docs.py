import chromadb


def embed_chunks(collection_name, chunks):
    client = chromadb.Client()
    collection = client.get_or_create_collection(collection_name)

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            ids=[str(i)]
        )

    return len(chunks)
