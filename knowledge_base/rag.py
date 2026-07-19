from .vector_store import search_chunks
from.llm import generate_answer



def ask_question(question, document_id):

    results = search_chunks(
        question,
        document_id
    )

    # print("RESULTS =", results)

    # chunks = results["documents"][0]

    # print("CHUNKS =", chunks)

    # context = "\n".join(chunks)
    chunks = results["documents"][0]

    print("CHUNKS =", chunks)

    # حذف Chunkهای تکراری
    chunks = list(dict.fromkeys(chunks))

    print("Unique Chunks =", len(chunks))
    
    if not chunks:
        return {
            "answer":"No relevant information was found in the selected document.",
            "sources":[]
        }

    context = "\n\n".join(chunks)

    answer = generate_answer(
        context,
        question
    )

    return {
        "answer": answer,
        "sources": chunks
    }
    
    
     
    