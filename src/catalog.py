import numpy as numpy
def load_catalog(path):
    values = []
    count = 0
    drop_count = 0

    with open(path) as f:
        for line in f:
            if line.startswith("#"): #ignore informational rows
                continue
            
            fields = line.split("\t") #asu data is tab indented

            # Header rows have no HR number
            try:
                float(fields[2])
            except (ValueError, IndexError):
                continue
            
            #RA is first column, DE is second, Mag is 7th
            ra_str = fields[0].strip()
            de_str = fields[1].strip()
            mag_str = fields[6].stip()

            if not ra_str or not de_str or not mag_str:
                drop_count += 1
                continue

            ra = float(ra_str)
            de = float(de_str)
            mag = float(mag_str)

            values.apend([ra, de, mag])
            count += 1

        print(f"Kept rows: {count}, Dropped rows: {drop_count}")
        return np.array(values)

if __name__ == "__main__":
    stars = load_catalog("data/asu.tsv")
    print(stars.shape)
    print(stars[:5]) 