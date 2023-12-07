#[path = "../modules/files.rs"]
mod files;

use std::env;
use std::collections::HashMap;
use std::cmp::Ordering;

#[derive(Debug, Clone, PartialEq, Default)]
struct Hand {
    value: String,
    bid: usize,
    hand_type: Type,
    rank: usize,
}

#[derive(Debug, Clone, PartialEq, Default)]
enum Type {
    #[default]
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind,
}

fn get_file() -> String {
    return if let Some(_arg1) = env::args().nth(1) {
        "full.txt".to_string()
    } else {
        "test.txt".to_string()
    };
}

fn main() {
    let values = files::read_lines(get_file())
        .unwrap()
        .map(|line| parse(line.unwrap()))
        .collect();

    part1(values);
    //part2(values);
}

fn part1(hands: Vec<Hand>) {
    let mut total_winnings = 0;

    let highcards = split_by_type_and_sort(&hands, Type::HighCard);
    let onepair = split_by_type_and_sort(&hands, Type::OnePair);
    let twopair = split_by_type_and_sort(&hands, Type::TwoPair);
    let threes = split_by_type_and_sort(&hands, Type::ThreeOfAKind);
    let fulls = split_by_type_and_sort(&hands, Type::FullHouse);
    let fours = split_by_type_and_sort(&hands, Type::FourOfAKind);
    let fives = split_by_type_and_sort(&hands, Type::FiveOfAKind);

    let mut start = 0;

    total_winnings += add_up(&highcards, start);
    //println!("part 1: {:?}", total_winnings);
    start = highcards.len();
    total_winnings += add_up(&onepair, start);
    start += onepair.len();
    total_winnings += add_up(&twopair, start);
    start += twopair.len();
    total_winnings += add_up(&threes, start);
    start += threes.len();
    total_winnings += add_up(&fulls, start);
    start += fulls.len();
    total_winnings += add_up(&fours, start);
    start += fours.len();
    // println!("part 1: {:?}", highcards);
    // println!("part 1: {:?}", onepair);
    // println!("part 1: {:?}", twopair);
    // println!("part 1: {:?}", threes);
    // println!("part 1: {:?}", fulls);
    // println!("part 1: {:?}", fours);
    // println!("part 1: {:?}", fives);
    //println!("part 1: {:?}", total_winnings);
    total_winnings += add_up(&fives, start);

    println!("part 1: {:?}", total_winnings);
   // println!("part 1: {:?}", fives);
}

fn split_by_type_and_sort(hands: &Vec<Hand>, hand_type: Type) -> Vec<&Hand> {
    let mut filtered = hands.iter().filter(|&n| n.hand_type == hand_type).collect::<Vec<&Hand>>();
    //println!("part 1: {:?}", filtered);
    filtered.sort_by(|a, b| sort_hands(a, b));
    //println!("part 1: {:?}", filtered);
    filtered
}

fn add_up(cards: &Vec<&Hand>, start: usize) -> usize {
    let mut winnings = 0usize;
    //println!("new card list");
    for (i, card) in cards.iter().enumerate() {
        //println!("{}", winnings);
        winnings += (i + 1 + start) * card.bid;
        //println!("{}", winnings);
    }
    winnings
}

fn sort_hands(a: &Hand, b: &Hand) -> Ordering {
    for i in 0..5 {
        let comparison = compare_card(a.value.as_bytes()[i] as char, b.value.as_bytes()[i] as char);
        if comparison != Ordering::Equal {
            return comparison;
        }
    }
    return Ordering::Equal;
}

fn compare_card(a: char, b: char) -> Ordering {
    if a == b {
        return Ordering::Equal;
    }

    let face_card = match (a, b) {
        ('A', _) => Ordering::Greater,
        (_, 'A') => Ordering::Less,
        ('K', _) => Ordering::Greater,
        (_, 'K') => Ordering::Less,
        ('Q', _) => Ordering::Greater,
        (_, 'Q') => Ordering::Less,
        ('J', _) => Ordering::Greater,
        (_, 'J') => Ordering::Less,
        ('T', _) => Ordering::Greater,
        (_, 'T') => Ordering::Less,
        (_, _) => Ordering::Equal
    };

    if face_card != Ordering::Equal {
        return face_card;
    }
    else {
        return a.to_string().parse::<usize>().unwrap().cmp(
            &b.to_string().parse::<usize>().unwrap());
    }
}

fn parse(value: String) -> Hand {
    let (hand, bid) = value.split_once(" ").unwrap();
    Hand {
        value: hand.to_string(),
        bid: bid.parse::<usize>().unwrap(),
        hand_type: check_type(hand),
        ..Default::default()
    }
}

fn check_type(value: &str) -> Type {
    let mut cards = get_card_types();

    for v in value.chars() {
        *cards.get_mut(&v).unwrap() += 1;
    }

    let max_count_key = cards
        .iter()
        .max_by(|a, b| a.1.cmp(&b.1))
        .unwrap();

    let max_count = max_count_key.1;

    let max_count_2 = cards
        .iter()
        .filter(|c| c.0 != max_count_key.0)
        .max_by(|a, b| a.1.cmp(&b.1))
        .map(|(_k, v)| v)
        .unwrap();

    return match (max_count, max_count_2) {
        (5, _) => Type::FiveOfAKind,
        (4, _) => Type::FourOfAKind,
        (3, 2) => Type::FullHouse,
        (3, _) => Type::ThreeOfAKind,
        (2, 2) => Type::TwoPair,
        (2, _) => Type::OnePair,
        (_, _) => Type::HighCard,
    }
}


fn get_card_types() -> HashMap<char, u16> {
    let mut cards = HashMap::new();
    cards.insert('A', 0);
    cards.insert('K', 0);
    cards.insert('Q', 0);
    cards.insert('J', 0);
    cards.insert('T', 0);
    cards.insert('9', 0);
    cards.insert('8', 0);
    cards.insert('7', 0);
    cards.insert('6', 0);
    cards.insert('5', 0);
    cards.insert('4', 0);
    cards.insert('3', 0);
    cards.insert('2', 0);
    return cards;
}
