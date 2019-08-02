import os, shutil
import pandas as pd
import numpy as np
from py_dataset import dataset


def build_collection(collection):
    # We start from scratch with a new dataset collection
    if os.path.isdir(collection):
        shutil.rmtree(collection)
    ok = dataset.init(collection)
    if ok == False:
        print("Dataset failed to init collection")
        exit()

    # Sync metdata from google sheet
    gsheet_id = '1er6yYk-7jcySyX7bqADIC_TrfSDTxwAwDh_hXSxSdoU'
    gsheet_name = 'data4tom'
    #The column for key values, starting at 1, in this case SRR
    id_col = 14 
    #Range of cells to import. This is basically all, can modify to exclude
    #portions of gsheet
    cell_range = "A1:ZZ"

    err = dataset.import_gsheet(collection, gsheet_id, gsheet_name, id_col, cell_range)
    if err != '':
        print(err)
        exit()

def add_files(collection):
    #Run through all elements in collection
    keys = dataset.keys(collection)
    for k in keys:
        record, err = dataset.read(collection,k)
        if err != '':
            print(err)
            exit()
        url = record['url_links']
        print('Processing file from ',url)
        #Make a dummy file to represent results from kallisto
        files = ['example_file'+k]
        for f in files:
            with open(f, "w") as file:
                file.write(" 0 1 0 "+k)
        #Now attach file to collection 
        err = dataset.attach(collection,k,files)
        if err != '':
            print(err)
            exit()
        #Cleanup local disk
        for f in files:
            os.remove(f)

def get_subset(collection):
    #Demo pulling out a subset of records from collection
    #Using pandas data feame
    #Get all files with cell type Xenotransplanted microglia
    keys = dataset.keys(collection)
    dot_paths = [".cell_source", ".species", ".tissue","._Key"]
    (grid, err) = dataset.grid(collection, keys, dot_paths)
    if err != "":
        print(err)
        exit()
    df = pd.DataFrame(np.array(grid), columns=["source", "species", "tissue","key"])
    grouped = df.groupby(["source"])
    print(grouped.groups.keys())
    records = grouped.get_group('Xenotransplanted microglia')
    for index, r in records.iterrows():
        print('getting files for ',r['key'])
        err = dataset.detach(collection,r['key'],[])
        if err != '':
            print(err)

    #Example doing the same thing with frames
    labels = ["source", "species", "tissue","key"]
    f, err = dataset.frame(collection, 'frame_name', keys, dot_paths, labels)
    if err != "":
        print(err)
    records = dataset.frame_objects(collection, 'frame_name')
    for record in records:
        if record['source'] == 'Xenotransplanted microglia':
            print('getting files for ',record['key'])
            err = dataset.detach(collection,record['key'],[])
            if err != '':
                print(err)

if __name__ == '__main__':
    collection = 'collection.ds'
    build_collection(collection)
    add_files(collection)
    get_subset(collection)
