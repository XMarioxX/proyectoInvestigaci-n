import {Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle} from "@/components/ui/card";
import {Separator} from "@/components/ui/separator";
import Link from "next/link";


export default function GlobalCard() {
    return(
        <>
            <h1>Hola desde el card</h1>
                <Card>
                    <Link href={"./hola"}>
                        <CardHeader className="space-y-4">
                            <CardTitle>Hola</CardTitle>
                            <CardDescription>Description</CardDescription>
                        </CardHeader>
                        <CardContent className="space-y-4">
                            <p>Contenido</p>
                            <Separator/>
                            <p>Contenido</p>
                        </CardContent>
                        <CardFooter>
                            Footer
                        </CardFooter>
                    </Link>
                </Card>
        </>
    )
}