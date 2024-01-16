import csv

file_to_load = "PyPoll/Resources/election_data.csv"
file_to_output = "election_analysis_csv.txt"

total_votes = 0
candidate_options =[]
candidate_votes = {}

winning_candidate = ""
winning_vote_count = 0

with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

            total_votes = total_votes + 1

            candidate_name = row["Candidate"]

            if candidate_name not in candidate_options:
               
                candidate_options.append(candidate_name)

                candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(file_to_output, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f".......................\n"
        f"Total Votes: {total_votes}\n"
        f".......................\n"

    )      
    print(election_results)    

    txt_file.write(election_results)

    for Candidate in candidate_votes:
          
        votes = candidate_votes.get(Candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_vote_count):
                winning_vote_count = votes
                winning_candidate = Candidate
        
        voter_output = f"{Candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)

        txt_file.write(voter_output)

    winning_candidate_summary = (
          f"...................\n"
          f"Winner: {winning_candidate}\n"
          f"...................\n"
    )
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)