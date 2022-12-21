class ChessBoard():
    def __init__(self):
        # mała litera - kolor, duża litera - figura
        # b - black/czarny, w - white/biały
        # R - Rook/Wieża, N - Knight/Skoczek, B - Bishop/Goniec, Q - Queen/Hetman, K - King/Król
        # "--" - oznacza pole puste
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []


