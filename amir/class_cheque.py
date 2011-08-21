
## \defgroup Controller
## @{

class ClassCheque:
    def __init__(self):
        pass

    ##
    #
    # @return list of spendable cheques or None
    def get_spendable_cheques(self):
        pass

    ## get the history of a single cheque
    #
    # @param id cheque id
    # @return histroy as a list
    def get_histroy(self, id):
        pass

    ## get cheque id from cheque number
    #
    # @param number Cheque Serial Number
    # @return cheque id

    ## Add Cheque to db
    #
    # @param information of new account as a dictionary
    def add_cheque(self, info):
        pass

    ## update cheque status
    #
    # updates cheque status and save last status in Cheque Histroy
    # \note You should call ClassCheque::save to save all changes or you will lose changes.
    # ChequeUI::save calls this function automatically.
    # @param id cheque id
    # @param status New status - Integer
    def update_status(self, id, status):
        pass

    ## Save datas to database
    def save(self):
        pass
## @}
