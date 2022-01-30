def get_delta(toponym):
    delta = str((abs(float(toponym["boundedBy"]['Envelope']["lowerCorner"].split()[0]) -
                     float(toponym["boundedBy"]['Envelope']['upperCorner'].split()[0])))) \
            + "," + \
            str(abs(float(toponym["boundedBy"]['Envelope']["lowerCorner"].split()[1]) -
                    float(toponym["boundedBy"]['Envelope']['upperCorner'].split()[1])))
    return delta
