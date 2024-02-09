from ai import get_completion

# CLI integration
def main():
    prompt = input('Enter prompt: ')
    response = get_completion(prompt)
    print(response)

if __name__ == "__main__":
    main()