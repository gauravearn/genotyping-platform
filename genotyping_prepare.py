#Gaurav Sablok 
#Senior Postdoctoral Fellow Faculty of Natural and Agricultural Sciences 
#Room 7-35, Agricultural Sciences Building 
#University of Pretoria, Private Bag X20 Hatfield 0028, 
#South Africa 
import os
import pandas as pd
def prepareTags(analysis_path, fasta_path):
    """
    a core function to prepare and tag the bacterial species or the 
    plant species for the genotyping platform based on the defined tags
    Arguments:
        path -- _give_the_path_to_the_fasta_files_
    """
    if !os.path.exists(analysis_path):
        os.mkdir(analysis_path)
        print(f"the directory for the analysis of the tags \
            model has been created")
    os.chdir(os.path.join(analysis_path))
    fasta_check = os.path.join(path)
    fasta_strings = []
    fasta_names = []
    for i in os.listdir(fasta_check):
        if i.endswith(".fasta") or i.endswith("*.fas"):
            with open(i, "r") as file:
                for line in file.readlines():
                    if line.startswith(">"):
                    fasta_names.append(line.strip().replace(">", ""))
                else:
                    fasta_strings.append(line.strip())
    fasta_dataframe = dict([(i,j) for i,j in zip(fasta_strings, fasta_names)]
    fasta_dataframe = pd.DataFrame(fasta_dict, sep = ",")
    classify = []
    while True:
        take_genotyping_tags = input("Please enter the tags for this dataset:")
        classify.append(take_genotyping_tags)
        if take_genotyping_tags is "":
            break
    def mapping_genotyping(x):
        for i in range(len(take_genotyping_tags)):
            if take_genotyping_tags[i] in x:
                return "mark_for_sequencing"
            if take_genotyping_tags[i] not in x:
                return "exclude"
    fasta_dataframe["genotyping_tags"] = fasta_dataframe["fasta_strings"].apply(mapping_genotyping)
    return dict([(i,j) for i,j in zip(fasta_strings, fasta_names)],
                classify, fasta_dataframe.info(), fasta_dataframe.columns,
                fasta["genotyping_tags"].value_counts()
    with open(sequencing_run, "w") as sequencing:
        sequencing.write(fasta_dataframe.to_csv())
        sequencing.close()
    if __name__== __main__:
        main()
