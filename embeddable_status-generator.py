from urllib.parse import quote


def generate_embeddable_status(jenkins_job_url):
    # Parse the input URL
    try:
        domain_url = jenkins_job_url.split("/job/")[0]
        path = jenkins_job_url.split(domain_url)[1]
        path = path.replace('/job/', '%2F')
        if path.endswith('/'):
           path = path[:-1]
        print(domain_url, path)
    except ValueError:
        raise ValueError("Invalid URL format. Ensure it's: <JENKINS-MAIN-DOMAIN>/<PATH-TO-JOB>/<NAME-OF-JOB>/")
    
    
    # Construct the embeddable status URL
    subject_encoded = quote(" Started: ${startTime} ago    ")
    embeddable_status = (
        f"{domain_url}/buildStatus/icon?"
        f"job={path}&"
        f"subject={subject_encoded}&"
        f"link={jenkins_job_url}"
    )
    
    return embeddable_status

if __name__ == "__main__":
    while True:
        job_url = input("Enter the full Jenkins job URL: ").strip()
        try:
            result = generate_embeddable_status(job_url)
            print("\nEmbeddable Status URL:")
            print(result)
            print("\n\n")
        except ValueError as e:
            print(f"Error: {e}")


