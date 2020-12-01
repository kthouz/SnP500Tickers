import pandas as pd

_RAW = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

def get_raw():
    return _RAW[0]

def extract_year(s):
    try:
        return int(str(s).split('-')[0])
    except:
        return None

class SPTickers():
    def __init__(self):
        self.raw = get_raw().reset_index().rename(columns={'index': 'rank'})
        self.raw.index = self.raw['Symbol']
        self.raw['hq_city'] = self.raw['Headquarters Location'].apply(lambda x: x.split(',')[0].strip())
        self.raw['hq_state'] = self.raw['Headquarters Location'].apply(lambda x: x.split(',')[1].strip())
        self.raw['year_added'] = self.raw['Date first added'].apply(lambda x: extract_year(x))

        self.symbols = self.raw['Security'].to_dict()
        self.gics_sectors = sorted(self.raw['GICS Sector'].unique().tolist())
        self.gics_sub_industries = sorted(self.raw['GICS Sub-Industry'].unique().tolist())

    def get_symbols_(self, gics_sector=None, gics_sub_industry=None, year_added=None, year_founded=None):
        return self.symbols

    def get_symbols(self, by=None, val=None):
        """
        return symbols and their names
        inputs
            :param by:(str), accepted values: "sector", "industry", "year_added", "year_founded". Default: None
            :param val: (str, int), value to filter by. Default: None
        """
        assert by in (None, "sector", "industry", "year_added", "year_founded")
        if by==None:
            return self.symbols
        if by=='sector':
            if val:
                return self.raw[self.raw['GICS Sector']==val]['Security'].to_dict()
            else:
                dct = self.raw.groupby('GICS Sector').agg({'Security': 'unique'}).to_dict(orient='index')
                for k, v in dct.items():
                    dct[k] = v['Security'].tolist()
                return dct
        if by=='industry':
            if val:
                return self.raw[self.raw['GICS Sub-Industry']==val]['Security'].to_dict()
            else:
                dct = self.raw.groupby('GICS Sub-Industry').agg({'Security': 'unique'}).to_dict(orient='index')
                for k, v in dct.items():
                    dct[k] = v['Security'].tolist()
                return dct
        if by=='year_added':
            if val:
                return self.raw[self.raw['year_added']==val]['Security'].to_dict()
            else:
                dct = self.raw.groupby('year_added').agg({'Security': 'unique'}).to_dict(orient='index')
                for k, v in dct.items():
                    dct[k] = v['Security'].tolist()
                return dct
        if by=='year_founded':
            if val:
                return self.raw[self.raw['Founded']==val]['Security'].to_dict()
            else:
                dct = self.raw.groupby('Founded').agg({'Security': 'unique'}).to_dict(orient='index')
                for k, v in dct.items():
                    dct[k] = v['Security'].tolist()
                return dct
        raise(Exception('[Error] Wrong value of `by`'))

    def get_sectors(self):
        return self.gics_sectors

    def get_industries(self):
        return self.gics_sub_industries

    def get_hq_location(self, symbol=None):
        pass

    def metadata(self, symbol):
        pass
